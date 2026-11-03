# Play-Annotation-Generator Annotation Review — SlantAndGo_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | SAF | `15` | `15` | 4 | START | 4 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `13` | 7 | START | 7 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 7 | START | 7 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 7 | START | 7 | 34 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 7 | START | 7 | 172 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `12` | `12` | 8 | START | 8 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 18 | END | 4 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | `12` | `12` | 85 | START | 85 | 164 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 100 | START | 100 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 99 | 81 | inferred_complete_timeline |
| `Action_ThrowPass` | 100 | 113 | 14 | inferred_complete_timeline |
| `Action_None` | 114 | 135 | 22 | inferred_complete_timeline |
| `Action_None` | 137 | 190 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 81 | 78 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SellRoute` | 8 | 84 | 77 | inferred_complete_timeline |
| `Action_VerticalStem` | 85 | 164 | 80 | inferred_complete_timeline |
| `Action_VerticalStem` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_VerticalStem` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_VerticalStem` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 191 | 188 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 173 | 170 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 34 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 194 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 177 | 171 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 239 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 191 | 185 | inferred_complete_timeline |
| `Action_PassBlock` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 207 | 216 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 172 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 48 | 55 | 8 | inferred_complete_timeline |
| `Action_None` | 57 | 135 | 79 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 135 | 132 | inferred_complete_timeline |
| `Action_None` | 137 | 144 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 158 | 13 | inferred_complete_timeline |
| `Action_None` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 159 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 187 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 122 | 119 | inferred_complete_timeline |
| `Action_None` | 149 | 161 | 13 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 138 | 135 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 159 | 15 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 19 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 201 | 198 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–175 | 167 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 39–51 | 12 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 41–97 | 57 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 83–239 | 136 | 5 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 111–120 | 10 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 121–206 | 50 | 7 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 221–239 | 17 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 16: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-128] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-81] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-201] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-190] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-187] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-135] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [85-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [166-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [183-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [203-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 19, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [19-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-191] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [194-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [207-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-158] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-173] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-194] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-97] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-134] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>