# Play-Annotation-Generator Annotation Review — Counter_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_24`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | TE1 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 100 | START | 100 | 114 |
| ✅ EXACT | `Action_DownBlock` | TE1 | `1` | `0` | 110 | START | 110 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `10` | 110 | START | 123 | 132 |
| ✅ EXACT | `Action_DownBlock` | LT | `6` | `5` | 110 | START | 110 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `9` | `8` | 110 | START | 110 | 146 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `14` | `13` | 110 | START | 110 | 217 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 115 | END | 100 | 115 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 130 | START | 130 | 147 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `4` | `3` | 148 | START | 216 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 217 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 115 | 16 | inferred_complete_timeline |
| `Action_None` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 130 | 147 | 18 | inferred_complete_timeline |
| `Action_None` | 148 | 186 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_BallCarry` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 155 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 198 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 155 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 131 | 32 | inferred_complete_timeline |
| `Action_None` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 269 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 123 | 132 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 217 | 80 | inferred_complete_timeline |
| `Action_None` | 218 | 223 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 146 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 149 | 217 | 69 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 110 | 217 | 108 | inferred_complete_timeline |
| `Action_None` | 218 | 229 | 12 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 140 | 41 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 232 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 213 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 113 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 124 | 25 | inferred_complete_timeline |
| `Action_None` | 126 | 197 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 145 | 46 | inferred_complete_timeline |
| `Action_None` | 148 | 269 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 134 | 35 | inferred_complete_timeline |
| `Action_None` | 140 | 165 | 26 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 183 | 84 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 244 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 118–269 | 130 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 157–269 | 113 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 164–198 | 31 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 194–269 | 76 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 200–206 | 5 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 230–232 | 3 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 232–269 | 35 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `4` (RB): Annotated start 148 != Inferred start 216

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (RG) duration 108 frames exceeds threshold 90 frames [start=110, end=217].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (C) duration 108 frames exceeds threshold 90 frames [start=110, end=217].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [100–115], lower_priority='Action_DownBlock' annotated_start=110, effective_Action_DownBlock_start=116.
- ⚠️ Action 'Action_DownBlock' range [110-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-198] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-155] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [110-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [100-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-232] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [110-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 218, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [218-229] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-197] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '26' has 1 frames without a visible bounding box.
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

</details>