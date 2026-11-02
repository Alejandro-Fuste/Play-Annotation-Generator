# Play-Annotation-Generator Annotation Review — JetSweep_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_95`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 187
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 114
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `24` | `22` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 3 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 3 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 82 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `16` | `15` | 83 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | Position_Unknown | `24` | `22` | 85 | START | 105 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 85 | START | 85 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 85 | START | 85 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 85 | START | 85 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 85 | START | 85 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 85 | START | 85 | 132 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 88 | START | 88 | 93 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 95 | END | 83 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 102 | START | 102 | 105 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `19` | `18` | 112 | START | N/A | N/A |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `5` | `4` | 112 | START | 112 | 153 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_Toss` | 102 | 105 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 179 | 11 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 294 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 105 | 23 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 208 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 121 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 132 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 143 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–23
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 23 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–197
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 84 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 151 | 14 | inferred_complete_timeline |
| `Action_None` | 154 | 184 | 31 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 111 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 112 | 153 | 42 | inferred_complete_timeline |
| `Action_None` | 154 | 178 | 25 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 225 | 42 | inferred_complete_timeline |
| `Action_None` | 231 | 256 | 26 | inferred_complete_timeline |
| `Action_None` | 258 | 275 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 115 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 124 | 42 | inferred_complete_timeline |
| `Action_None` | 126 | 173 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 92 | 138 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 141 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 178 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 246 | 164 | inferred_complete_timeline |
| `Action_None` | 249 | 268 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 235 | 153 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 291 | 43 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 305 | 5 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_None` | 312 | 317 | 6 | inferred_complete_timeline |
| `Action_None` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 333 | 6 | inferred_complete_timeline |
| `Action_None` | 336 | 389 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 70–150 | 77 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 88–93 | 6 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 89–156 | 68 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 97–133 | 15 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 101–119 | 10 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 105–389 | 214 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 109–389 | 248 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 121–136 | 16 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 131–221 | 72 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 137–389 | 243 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 146–163 | 16 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 147–192 | 40 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 152–181 | 26 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 194–318 | 111 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 198–271 | 73 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 213–254 | 42 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 221–389 | 153 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 237–284 | 48 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 238–389 | 150 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 244–367 | 94 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 257–294 | 38 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 266–369 | 93 | 3 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 267–389 | 123 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 271–345 | 75 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 275–288 | 14 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 280–301 | 22 | 1 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 291–389 | 99 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 298–389 | 92 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 309–314 | 6 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 313–389 | 63 | 2 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 354–367 | 14 | 1 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 354–383 | 13 | 2 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 362–389 | 28 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 373–378 | 6 | 1 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `24` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=83, end=23. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=85, end=23. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '18' has invalid range: start=112, end=93. Clamping end to start.
- ⚠️ Action 'Action_None' range [83-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-246] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-256] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-294] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-173] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [102-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-23] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [88-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [105-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [116-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-389] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-136] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-264] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-284] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-169] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-181] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-271] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-254] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-290] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-353] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-379] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-287] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-389] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-322] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-367] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-294] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-348] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-363] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-345] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-301] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-353] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-367] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-361] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-378] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.

</details>