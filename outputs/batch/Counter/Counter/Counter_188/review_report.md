# Play-Annotation-Generator Annotation Review — Counter_188

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_188`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `16` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `16` | `13` |
| ✅ EXACT | `Action_DownBlock` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | CB1 | defense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | CB2 | defense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | LB1 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB2 | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 8 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 24 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 128 |
| ✅ EXACT | `Action_BallSnap` | LT | `16` | `13` | 127 | START | 127 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | `11` | `10` | 129 | START | 129 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `16` | `13` | 129 | START | 129 | 131 |
| ✅ EXACT | `Action_DownBlock` | WR2 | `2` | `1` | 129 | START | 129 | 179 |
| ✅ EXACT | `Action_PullBlock` | RB | `8` | `7` | 129 | START | 129 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | CB1 | `4` | `3` | 129 | START | 129 | 149 |
| ✅ EXACT | `Action_PlaySideFakeStep` | CB2 | `5` | `4` | 131 | START | 131 | 168 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `10` | `9` | 139 | END | 127 | 139 |
| ✅ EXACT | `Action_Handoff` | LB1 | `10` | `9` | 148 | START | 148 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB2 | `5` | `4` | 172 | START | 178 | 191 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 24–128
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 53 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 208 | 80 | inferred_complete_timeline |
| `Action_None` | 209 | 230 | 22 | inferred_complete_timeline |
| `Action_None` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 299 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 179 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 202 | 76 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_None` | 223 | 289 | 67 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 8–182
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 60 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 115 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 139 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 179 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 159–275
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 159 | 212 | 54 | inferred_complete_timeline |
| `Action_None` | 215 | 275 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 164 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 146 | 20 | inferred_complete_timeline |
| `Action_None` | 156 | 186 | 31 | inferred_complete_timeline |
| `Action_None` | 234 | 272 | 39 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 206 | 80 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 292 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 148 | 171 | 24 | inferred_complete_timeline |
| `Action_None` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 152 | 208 | 57 | inferred_complete_timeline |
| `Action_None` | 209 | 299 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 131 | 168 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 191 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 161 | 35 | inferred_complete_timeline |
| `Action_None` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 205 | 26 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 155 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 169 | 208 | 40 | inferred_complete_timeline |
| `Action_None` | 210 | 219 | 10 | inferred_complete_timeline |
| `Action_None` | 224 | 256 | 33 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `21` | Position_Unknown | Team_Unknown | 152–299 | 132 | 4 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 168–299 | 96 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 169–200 | 18 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 181–293 | 112 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 188–194 | 7 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 190–299 | 86 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 227–294 | 67 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 229–265 | 28 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 233–299 | 52 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 241–299 | 41 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 268–281 | 11 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [129-179] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [129-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [131-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-289] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-208] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-230] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-256] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-272] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-115] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-179] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-53] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-275] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-288] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-291] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-275] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '29' has 1 frames without a visible bounding box.
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

</details>