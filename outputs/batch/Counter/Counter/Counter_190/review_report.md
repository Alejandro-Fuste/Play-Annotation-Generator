# Play-Annotation-Generator Annotation Review — Counter_190

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_190`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `21` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | SAF2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | CB3 | defense | `15` | `14` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB2 | defense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 95 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 121 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 142 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 172 |
| ✅ EXACT | `Action_BallSnap` | LG | `21` | `18` | 173 | START | 173 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `18` | 174 | START | 174 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | `3` | `2` | 174 | START | 174 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | `3` | `2` | 174 | START | 174 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | SAF2 | `13` | `12` | 174 | START | 174 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | CB3 | `15` | `14` | 174 | START | 174 | 216 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB2 | `6` | `5` | 179 | START | 179 | 211 |
| ✅ EXACT | `Action_SnapReceive` | RB | `14` | `13` | 182 | END | 173 | 182 |
| ✅ EXACT | `Action_Handoff` | RB | `14` | `13` | 197 | START | 197 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | `6` | `5` | 212 | START | 212 | 219 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 251 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 142–329
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 142 | 172 | 31 | inferred_complete_timeline |
| `Action_None` | 173 | 261 | 89 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_SnapReceive` | 173 | 182 | 10 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 197 | 211 | 15 | inferred_complete_timeline |
| `Action_None` | 212 | 297 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 172 | 90 | inferred_complete_timeline |
| `Action_None` | 173 | 238 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 173 | 130 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 206 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 211 | 251 | 41 | inferred_complete_timeline |
| `Action_None` | 252 | 282 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 190 | 18 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 183 | 11 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 121–182
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 121 | 137 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 172 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 173 | 173 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 174 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 95–219
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 95 | 172 | 78 | inferred_complete_timeline |
| `Action_None` | 173 | 200 | 28 | inferred_complete_timeline |
| `Action_None` | 205 | 219 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 95 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 172 | 75 | inferred_complete_timeline |
| `Action_None` | 173 | 215 | 43 | inferred_complete_timeline |
| `Action_None` | 217 | 240 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 172 | 140 | inferred_complete_timeline |
| `Action_None` | 173 | 213 | 41 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 228 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 172 | 122 | inferred_complete_timeline |
| `Action_None` | 173 | 183 | 11 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 179 | 211 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 30 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 172 | 118 | inferred_complete_timeline |
| `Action_None` | 173 | 201 | 29 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |
| `Action_None` | 302 | 318 | 17 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 304 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 173 | 92 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 174 | 216 | 43 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 218 | 251 | 34 | inferred_complete_timeline |
| `Action_None` | 252 | 329 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 91–191
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 91 | 172 | 82 | inferred_complete_timeline |
| `Action_None` | 173 | 191 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 173 | 98 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 194 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 199 | 222 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 226 | 251 | 26 | inferred_complete_timeline |
| `Action_None` | 252 | 329 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 173–206 | 28 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 205–212 | 7 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 215–329 | 114 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 223–329 | 96 | 5 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 231–236 | 6 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 242–329 | 71 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 244–329 | 78 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 264–329 | 66 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 280–329 | 43 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 284–329 | 46 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 296–329 | 34 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 326–329 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Deduplicated duplicate event 'Action_DownBlock' at frame 174 for track '2'.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-238] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-318] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [211-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [179-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-329] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-304] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [199-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [226-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [174-216] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-200] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-219] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-137] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '18' starts at frame 174, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [174-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-261] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-327] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-244] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-329] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '36' has 1 frames without a visible bounding box.
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