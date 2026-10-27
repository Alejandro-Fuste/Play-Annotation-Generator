# Play-Annotation-Generator Annotation Review — Counter_187

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_187`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LB2 | defense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB1 | defense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 99 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `21` | `20` | 100 | START | 100 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 105 | START | 105 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 105 | START | 105 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 105 | START | 105 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 105 | START | 105 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LB2 | `9` | `8` | 105 | START | 105 | 143 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB1 | `6` | `5` | 107 | START | 107 | 142 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `20` | `19` | 113 | END | 100 | 113 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `20` | `19` | 122 | START | 122 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | `6` | `5` | 143 | START | 143 | 149 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 215 | 116 | inferred_complete_timeline |
| `Action_None` | 220 | 247 | 28 | inferred_complete_timeline |
| `Action_None` | 254 | 265 | 12 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 230 | 131 | inferred_complete_timeline |
| `Action_None` | 237 | 263 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 170 | 71 | inferred_complete_timeline |
| `Action_None` | 175 | 215 | 41 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 176 | 77 | inferred_complete_timeline |
| `Action_None` | 185 | 207 | 23 | inferred_complete_timeline |
| `Action_None` | 212 | 218 | 7 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 165 | 66 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 184 | 85 | inferred_complete_timeline |
| `Action_None` | 191 | 269 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 107 | 142 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 105 | 143 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 150 | 160 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–269 | 260 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–269 | 268 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–171 | 160 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–269 | 254 | 9 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–269 | 268 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–137 | 132 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–269 | 269 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–176 | 168 | 8 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–243 | 225 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 144–269 | 123 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 144–269 | 124 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 170–259 | 76 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 175–269 | 90 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 203–206 | 4 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 222–269 | 37 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 240–244 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 66 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [100-176] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-207] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-263] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [105-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [150-160] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-247] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-184] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-265] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-236] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-217] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-254] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [156-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-176] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-178] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [181-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-263] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-259] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>