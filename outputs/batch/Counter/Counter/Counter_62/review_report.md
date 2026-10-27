# Play-Annotation-Generator Annotation Review — Counter_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_62`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | TE | offense | `17` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 9 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 14 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `15` | `14` | 130 | START | 130 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `10` | `9` | 132 | START | 132 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `6` | `5` | 132 | START | 132 | 174 |
| ✅ EXACT | `Action_PullBlock` | LG | `12` | `11` | 132 | START | 132 | 152 |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | TE | `17` | `15` | 132 | START | 136 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 146 | END | 130 | 146 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 157 | START | 157 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `12` | 175 | START | 175 | 176 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 212 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_SnapReceive` | 130 | 146 | 17 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 174 | 18 | inferred_complete_timeline |
| `Action_None` | 175 | 269 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 81 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 14–170
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 25 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 34 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 136 | 170 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 154 | 25 | inferred_complete_timeline |
| `Action_None` | 165 | 174 | 10 | inferred_complete_timeline |
| `Action_None` | 194 | 205 | 12 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PullBlock` | 132 | 152 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 129 | 121 | inferred_complete_timeline |
| `Action_BallSnap` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 136 | 146 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 225 | 79 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 147 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 212 | 55 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 174 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 187 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 212 | 16 | inferred_complete_timeline |
| `Action_None` | 213 | 233 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |
| `Action_None` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 207 | 9 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 184 | 55 | inferred_complete_timeline |
| `Action_None` | 189 | 216 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 190 | 61 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 217 | 88 | inferred_complete_timeline |
| `Action_None` | 219 | 234 | 16 | inferred_complete_timeline |
| `Action_None` | 237 | 269 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 235 | 106 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–142 | 134 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 83–141 | 55 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 101–107 | 6 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 140–185 | 34 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 146–174 | 22 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 199–229 | 29 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 206–269 | 47 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 209–255 | 41 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 212–255 | 44 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 220–269 | 22 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 224–263 | 31 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 226–237 | 12 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 228–237 | 10 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 229–232 | 4 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 247–269 | 23 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 249–269 | 21 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 250–269 | 20 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ `Action_PullLeadBlock` for actor_track_id `17` (TE): Annotated start 132 != Inferred start 136
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 126: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [130-217] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-216] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [157-174] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [132-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [130-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-225] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-25] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [136-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-219] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-251] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>