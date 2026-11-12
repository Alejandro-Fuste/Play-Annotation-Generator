# Play-Annotation-Generator Annotation Review — SplitZone_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_14`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 1
- **Action Segments:** 108
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 15 | START | 15 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 15 | START | 15 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 15 | START | 15 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 15 | START | 15 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 15 | START | 15 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 15 | START | 15 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 15 | START | 15 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 15 | START | 15 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 15 | START | 15 | 131 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `6` | 125 | START | 125 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 128 | START | 128 | 209 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 128 | START | 128 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 128 | START | 128 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 128 | START | 128 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `6` | 128 | START | 143 | 144 |
| ✅ EXACT | `Action_SplitBlock` | HB | `9` | `9` | 132 | START | 132 | 209 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 142 | END | 125 | 142 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 150 | START | 150 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `10` | 170 | START | 170 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 209 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_SnapReceive` | 125 | 142 | 18 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 150 | 169 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 235 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–173
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_None` | 125 | 173 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 15–247
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 131 | 117 | inferred_complete_timeline |
| `Action_SplitBlock` | 132 | 209 | 78 | inferred_complete_timeline |
| `Action_None` | 210 | 247 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–321
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_None` | 125 | 313 | 189 | inferred_complete_timeline |
| `Action_None` | 318 | 321 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–193
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 127 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 193 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 15–193
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 127 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 154 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 193 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 15–235
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_BallSnap` | 125 | 142 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 209 | 64 | inferred_complete_timeline |
| `Action_None` | 210 | 235 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 15–191
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 127 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 183 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–292
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 127 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 209 | 82 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |
| `Action_None` | 240 | 282 | 43 | inferred_complete_timeline |
| `Action_None` | 284 | 292 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 15–176
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_None` | 125 | 176 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–179
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 164 | 40 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 29–212
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 124 | 96 | inferred_complete_timeline |
| `Action_None` | 125 | 128 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 212 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 40–180
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 40 | 124 | 85 | inferred_complete_timeline |
| `Action_None` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 168 | 30 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 124 | 78 | inferred_complete_timeline |
| `Action_None` | 125 | 144 | 20 | inferred_complete_timeline |
| `Action_None` | 148 | 242 | 95 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 278 | 22 | inferred_complete_timeline |
| `Action_None` | 281 | 329 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–170
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_None` | 125 | 144 | 20 | inferred_complete_timeline |
| `Action_None` | 149 | 164 | 16 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 36–329
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 124 | 65 | inferred_complete_timeline |
| `Action_None` | 125 | 184 | 60 | inferred_complete_timeline |
| `Action_None` | 186 | 204 | 19 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_None` | 252 | 277 | 26 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–203
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_None` | 125 | 198 | 74 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `24` | Position_Unknown | Team_Unknown | 80–143 | 27 | 5 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 153–239 | 82 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 157–161 | 5 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 161–265 | 89 | 2 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 179–284 | 106 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 183–196 | 12 | 2 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 184–239 | 56 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 200–268 | 48 | 3 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 203–292 | 84 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 203–275 | 71 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 210–252 | 43 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 214–223 | 10 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 227–329 | 103 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 230–270 | 35 | 2 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 241–329 | 87 | 3 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 260–329 | 69 | 2 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 287–329 | 43 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 303–329 | 11 | 4 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | 15 | 19 | 5 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [125–142], lower_priority='Action_ZoneBlock' annotated_start=128, effective_Action_ZoneBlock_start=143.
- ⚠️ Action 'Action_None' range [210-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-282] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-313] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-183] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-198] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-173] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-164] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-45] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-124] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-242] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-329] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-204] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-277] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-168] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-265] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-284] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-239] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-292] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-258] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-316] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-327] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-321] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '35' has 1 frames without a visible bounding box.
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

</details>