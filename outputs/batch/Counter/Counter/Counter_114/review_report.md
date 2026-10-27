# Play-Annotation-Generator Annotation Review — Counter_114

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_114`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 170
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 114
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE1 | defense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 99 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 99 | START | 99 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 100 | START | 111 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 100 | START | 100 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `7` | `6` | 100 | START | 100 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `12` | `11` | 100 | START | 100 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE1 | `15` | `14` | 100 | START | 100 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 110 | END | 99 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `10` | `9` | 122 | START | 122 | 125 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `11` | `10` | 140 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 175 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–140
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 110 | 12 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 140 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 120 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 151 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 175 | 12 | inferred_complete_timeline |
| `Action_None` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 218 | 29 | inferred_complete_timeline |
| `Action_None` | 220 | 247 | 28 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 329 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 51 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 104 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 175 | 17 | inferred_complete_timeline |
| `Action_None` | 176 | 185 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 110 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 142 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 175 | 19 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_None` | 190 | 199 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 111 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 100 | 136 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 147 | 173 | 27 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 175 | 175 | 1 | inferred_complete_timeline |
| `Action_None` | 176 | 186 | 11 | inferred_complete_timeline |
| `Action_None` | 195 | 272 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 138 | 40 | inferred_complete_timeline |
| `Action_None` | 142 | 167 | 26 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 270 | 65 | inferred_complete_timeline |
| `Action_None` | 273 | 296 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 178 | 80 | inferred_complete_timeline |
| `Action_None` | 208 | 218 | 11 | inferred_complete_timeline |
| `Action_None` | 225 | 244 | 20 | inferred_complete_timeline |
| `Action_None` | 249 | 308 | 60 | inferred_complete_timeline |
| `Action_None` | 310 | 317 | 8 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 171 | 73 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 211 | 113 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 329 | 231 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 5–276 | 259 | 5 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 56–128 | 73 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 67–193 | 97 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 119–227 | 102 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 124–327 | 177 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 132–225 | 78 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 148–329 | 182 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 154–329 | 165 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 165–265 | 90 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 172–290 | 102 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 182–251 | 56 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 191–217 | 23 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 193–269 | 37 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 199–258 | 54 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 209–329 | 118 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 213–329 | 117 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 219–299 | 78 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 222–242 | 21 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 232–277 | 37 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 235–302 | 57 | 5 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 241–329 | 86 | 3 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 260–329 | 70 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 280–318 | 29 | 3 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 289–329 | 41 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 295–329 | 35 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `11` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '10' has invalid range: start=140, end=125. Clamping end to start.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [99–110], lower_priority='Action_DownBlock' annotated_start=100, effective_Action_DownBlock_start=111.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-329] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-178] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-308] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-270] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-296] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-247] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [122-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [128-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 140, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [140-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [99-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-51] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [100-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [147-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-204] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-98] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-96] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-217] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-157] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-327] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-329] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-265] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-290] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-217] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-294] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-329] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-259] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-283] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-255] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-306] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-318] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-329] for track '40' has 2 frames without a visible bounding box.
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

</details>