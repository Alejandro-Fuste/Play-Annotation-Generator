# Play-Annotation-Generator Annotation Review — Counter_150

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_150`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 135 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `22` | `21` | 136 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | QB | `14` | `13` | 137 | START | 137 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 137 | START | 142 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 137 | START | 137 | 176 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `11` | 137 | START | 137 | 162 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `6` | `5` | 137 | START | 137 | 178 |
| ✅ EXACT | `Action_SnapReceive` | LG | `4` | `3` | 150 | END | 136 | 150 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 155 | START | 155 | 173 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 174 | START | 174 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 206 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 154 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 155 | 173 | 19 | inferred_complete_timeline |
| `Action_None` | 174 | 244 | 71 | inferred_complete_timeline |
| `Action_None` | 246 | 273 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 178 | 43 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_None` | 204 | 218 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 176 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_None` | 207 | 236 | 30 | inferred_complete_timeline |
| `Action_None` | 242 | 254 | 13 | inferred_complete_timeline |
| `Action_None` | 258 | 299 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_SnapReceive` | 136 | 150 | 15 | inferred_complete_timeline |
| `Action_None` | 151 | 168 | 18 | inferred_complete_timeline |
| `Action_None` | 172 | 184 | 13 | inferred_complete_timeline |
| `Action_None` | 193 | 205 | 13 | inferred_complete_timeline |
| `Action_None` | 207 | 216 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PullBlock` | 137 | 162 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 137 | 178 | 42 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_None` | 164 | 254 | 91 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 114 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 135 | 20 | inferred_complete_timeline |
| `Action_None` | 136 | 136 | 1 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 225 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_None` | 154 | 166 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 211 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 135 | 79 | inferred_complete_timeline |
| `Action_None` | 136 | 189 | 54 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 183 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 135 | 44 | inferred_complete_timeline |
| `Action_None` | 136 | 179 | 44 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 230 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 236 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–201 | 194 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 22–35 | 14 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 25–43 | 18 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 35–159 | 68 | 10 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 109–177 | 14 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 142–299 | 75 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 151–184 | 28 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 164–299 | 129 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 170–299 | 125 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 173–200 | 16 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 185–299 | 104 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 217–238 | 22 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 228–299 | 72 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 229–258 | 30 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 271–299 | 14 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 272–299 | 28 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 275–285 | 11 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 282–299 | 18 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 283–297 | 13 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `22` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 81 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [136-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-168] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-176] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [137-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-135] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 136, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [136-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-162] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [137-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-211] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-35] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-43] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-85] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 136, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [136-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-115] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-200] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>