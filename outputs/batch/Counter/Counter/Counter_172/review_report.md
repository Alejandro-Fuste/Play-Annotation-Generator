# Play-Annotation-Generator Annotation Review — Counter_172

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_172`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 3
- **Action Segments:** 99
- **Validation Warnings:** 92
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
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB1 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | DE1 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE2 | defense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | SAF | defense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 4 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `23` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 101 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `11` | `10` | 102 | START | 102 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB1 | `10` | `9` | 108 | START | 108 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB1 | `11` | `10` | 108 | START | 108 | 191 |
| ✅ EXACT | `Action_DownBlock` | DE1 | `12` | `11` | 108 | START | 108 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `15` | `14` | 108 | START | 108 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE2 | `4` | `3` | 108 | START | 108 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RT | `13` | `12` | 116 | START | 116 | 139 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `8` | `7` | 118 | END | 102 | 118 |
| ✅ EXACT | `Action_Handoff` | SAF | `8` | `7` | 129 | START | 129 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `13` | `12` | 143 | START | 144 | 155 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `23`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 164–269
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 164 | 253 | 90 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 131 | 30 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 177 | 263 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 172 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 149–269
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 149 | 196 | 48 | inferred_complete_timeline |
| `Action_None` | 211 | 221 | 11 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 158–185
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 158 | 185 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 178–180
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 36 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 101 | 54 | inferred_complete_timeline |
| `Action_None` | 102 | 269 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 74 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 115 | 21 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 116 | 139 | 24 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 238 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 159 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 140 | 33 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 145 | 154 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–198
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 107 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 127 | 189 | 63 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 119 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 177 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_None` | 192 | 234 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 269 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 191 | 84 | inferred_complete_timeline |
| `Action_None` | 192 | 221 | 30 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 142 | 41 | inferred_complete_timeline |
| `Action_None` | 144 | 160 | 17 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_None` | 198 | 260 | 63 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 102 | 118 | 17 | inferred_complete_timeline |
| `Action_None` | 119 | 124 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 142 | 14 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 185 | 18 | inferred_complete_timeline |
| `Action_None` | 192 | 214 | 23 | inferred_complete_timeline |
| `Action_None` | 217 | 260 | 44 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 133 | 32 | inferred_complete_timeline |
| `Action_None` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 138 | 29 | inferred_complete_timeline |
| `Action_None` | 154 | 211 | 58 | inferred_complete_timeline |
| `Action_None` | 213 | 246 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `25` | Position_Unknown | Team_Unknown | 180–190 | 11 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 187–269 | 83 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 192–269 | 78 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 196–269 | 74 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 208–213 | 6 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 216–250 | 30 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 218–263 | 37 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 251–269 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `30` | 199 | 204 | 4 | 66.7% | 200–201 |
| `24` | `33` | 201 | 201 | 1 | 100.0% | None |
| `30` | `43` | 256 | 256 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [102-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-133] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-211] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [145-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-260] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [129-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-214] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-260] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-177] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-221] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [116-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [141-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [108-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [127-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-253] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-190] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-240] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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