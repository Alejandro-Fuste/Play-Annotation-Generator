# Play-Annotation-Generator Annotation Review — JetSweep_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_77`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 139
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_SealBlock` | TE | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 71 | START | 71 | 84 |
| ✅ EXACT | `Action_LeadBlock` | RB | `13` | `12` | 72 | START | 72 | 168 |
| ✅ EXACT | `Action_SealBlock` | TE | `12` | `11` | 72 | START | 72 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 72 | START | 85 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 72 | START | 72 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `13` | 72 | START | 72 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 72 | START | 72 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 72 | START | 72 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `18` | `15` | 74 | START | 74 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 84 | END | 71 | 84 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 91 | START | 91 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `15` | 102 | START | 102 | 155 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 168 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 84 | 14 | inferred_complete_timeline |
| `Action_None` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_Toss` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_None` | 103 | 130 | 28 | inferred_complete_timeline |
| `Action_None` | 132 | 266 | 135 | inferred_complete_timeline |
| `Action_None` | 269 | 281 | 13 | inferred_complete_timeline |
| `Action_None` | 283 | 389 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_LeadBlock` | 72 | 168 | 97 | inferred_complete_timeline |
| `Action_None` | 169 | 193 | 25 | inferred_complete_timeline |
| `Action_None` | 197 | 320 | 124 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 340 | 4 | inferred_complete_timeline |
| `Action_None` | 342 | 344 | 3 | inferred_complete_timeline |
| `Action_None` | 347 | 350 | 4 | inferred_complete_timeline |
| `Action_None` | 355 | 389 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SealBlock` | 72 | 141 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 111 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 82 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 84 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 119 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 168 | 86 | inferred_complete_timeline |
| `Action_None` | 169 | 218 | 50 | inferred_complete_timeline |
| `Action_None` | 223 | 288 | 66 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 109 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 206 | 136 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 359 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 128 | 58 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 246 | 176 | inferred_complete_timeline |
| `Action_None` | 252 | 389 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 216 | 146 | inferred_complete_timeline |
| `Action_None` | 223 | 231 | 9 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 277 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |
| `Action_None` | 182 | 201 | 20 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 96 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 389 | 319 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 74–389 | 284 | 12 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 86–389 | 282 | 5 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 89–389 | 286 | 9 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 105–125 | 21 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 121–389 | 263 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 132–208 | 76 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 132–389 | 245 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 146–389 | 229 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 149–389 | 236 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 164–389 | 226 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 186–208 | 16 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 199–389 | 186 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 201–389 | 189 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 204–212 | 7 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 208–389 | 146 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 224–389 | 160 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 237–389 | 153 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 239–389 | 139 | 4 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 241–389 | 149 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 258–314 | 54 | 3 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 272–389 | 112 | 3 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 273–294 | 11 | 2 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 321–324 | 4 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 378–389 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | 81 | 83 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [71–84], lower_priority='Action_ZoneBlock' annotated_start=72, effective_Action_ZoneBlock_start=85.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '12' (RB) duration 97 frames exceeds threshold 90 frames [start=72, end=168].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 97 frames exceeds threshold 90 frames [start=72, end=168].
- ⚠️ Action 'Action_None' range [71-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-100] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-277] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [91-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-266] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-281] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-389] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-246] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [72-141] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-320] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-218] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-288] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [74-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [88-94] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [96-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-155] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-334] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-356] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-252] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-312] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-341] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-267] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-198] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-375] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-330] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-244] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-389] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-355] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-381] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-389] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-283] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-314] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-389] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>