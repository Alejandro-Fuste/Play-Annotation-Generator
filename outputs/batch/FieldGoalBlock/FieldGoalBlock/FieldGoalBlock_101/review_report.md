# Play-Annotation-Generator Annotation Review — FieldGoalBlock_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_101`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `21` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `8` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 20 | START | 20 | 31 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 50 | START | 50 | 56 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `21` | `18` | 56 | START | 56 | 67 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PlaceBall` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_KickBall` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 57 | 299 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 91 | 126 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 152 | 103 | inferred_complete_timeline |
| `Action_None` | 156 | 161 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 88 | 130 | 43 | inferred_complete_timeline |
| `Action_None` | 132 | 299 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 273 | 224 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 128 | 79 | inferred_complete_timeline |
| `Action_None` | 134 | 199 | 66 | inferred_complete_timeline |
| `Action_None` | 282 | 298 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 245 | 196 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 195 | 146 | inferred_complete_timeline |
| `Action_None` | 200 | 276 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 125 | 76 | inferred_complete_timeline |
| `Action_None` | 131 | 140 | 10 | inferred_complete_timeline |
| `Action_None` | 152 | 160 | 9 | inferred_complete_timeline |
| `Action_None` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 245 | 64 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 35 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 49 | 13 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 56 | 81 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 21 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 93 | 30 | inferred_complete_timeline |
| `Action_None` | 95 | 286 | 192 | inferred_complete_timeline |
| `Action_None` | 288 | 295 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 49 | 11 | inferred_complete_timeline |
| `Action_None` | 50 | 160 | 111 | inferred_complete_timeline |
| `Action_None` | 174 | 257 | 84 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 276 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 80 | 31 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 193 | 103 | inferred_complete_timeline |
| `Action_None` | 196 | 212 | 17 | inferred_complete_timeline |
| `Action_None` | 221 | 284 | 64 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 84 | 35 | inferred_complete_timeline |
| `Action_None` | 88 | 121 | 34 | inferred_complete_timeline |
| `Action_None` | 125 | 204 | 80 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_None` | 212 | 261 | 50 | inferred_complete_timeline |
| `Action_None` | 272 | 299 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 224 | 175 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `21` | Position_Unknown | Team_Unknown | 26–110 | 66 | 4 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 65–125 | 61 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 74–275 | 192 | 5 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 79–245 | 167 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 91–299 | 170 | 5 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 100–282 | 179 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 113–228 | 113 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 134–299 | 166 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 139–144 | 6 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 140–299 | 142 | 7 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 145–299 | 152 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 165–299 | 135 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 234–250 | 17 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 246–268 | 23 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 249–299 | 36 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 255–268 | 14 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 260–274 | 14 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 95 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [50-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-152] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-84] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-121] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-245] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-273] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-257] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-193] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-284] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-35] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-81] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-89] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-200] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-275] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-263] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-282] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-225] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-197] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-212] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '36' has 1 frames without a visible bounding box.
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