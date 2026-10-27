# Play-Annotation-Generator Annotation Review — Counter_224

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_224`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 101 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 100 | START | 100 | 116 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `11` | `10` | 102 | START | 117 | 117 |
| ✅ EXACT | `Action_DownBlock` | RT | `14` | `13` | 102 | START | 102 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `7` | 102 | START | 102 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `17` | `16` | 102 | START | 102 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `2` | `1` | 107 | START | 107 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 116 | END | 100 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 134 | START | 134 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 155 | START | 155 | 272 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 194 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 117 | 133 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 134 | 154 | 21 | inferred_complete_timeline |
| `Action_None` | 155 | 240 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 107 | 151 | 45 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 154 | 154 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 272 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 277 | 299 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 216 | 117 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 102 | 130 | 29 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 134 | 194 | 61 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 147 | 48 | inferred_complete_timeline |
| `Action_None` | 157 | 227 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 134 | 35 | inferred_complete_timeline |
| `Action_None` | 137 | 146 | 10 | inferred_complete_timeline |
| `Action_None` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_None` | 164 | 170 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 214 | 42 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 117 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PullBlock` | 102 | 164 | 63 | inferred_complete_timeline |
| `Action_PullBlock` | 170 | 194 | 25 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 194 | 93 | inferred_complete_timeline |
| `Action_None` | 195 | 230 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 134 | 35 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 170 | 30 | inferred_complete_timeline |
| `Action_None` | 173 | 192 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 299 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 117 | 18 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 186 | 52 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |
| `Action_None` | 230 | 282 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 132 | 33 | inferred_complete_timeline |
| `Action_None` | 138 | 156 | 19 | inferred_complete_timeline |
| `Action_None` | 158 | 173 | 16 | inferred_complete_timeline |
| `Action_None` | 175 | 187 | 13 | inferred_complete_timeline |
| `Action_None` | 194 | 199 | 6 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 174 | 75 | inferred_complete_timeline |
| `Action_None` | 179 | 291 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 135 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 143 | 44 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 173 | 74 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 120–226 | 107 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 129–299 | 165 | 3 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 146–299 | 138 | 5 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 148–299 | 152 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 175–299 | 124 | 2 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 197–299 | 72 | 4 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 211–299 | 85 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 230–299 | 70 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 233–276 | 34 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `11` (C): Annotated start 102 != Inferred start 117
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (RG) duration 93 frames exceeds threshold 90 frames [start=102, end=194].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [100–116], lower_priority='Action_DownBlock' annotated_start=102, effective_Action_DownBlock_start=117.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RT) duration 93 frames exceeds threshold 90 frames [start=102, end=194].
- ⚠️ Action 'Action_None' range [100-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-214] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [107-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-272] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-216] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [102-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '10' starts at frame 117, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [117-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-227] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [102-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-175] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-230] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-241] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
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