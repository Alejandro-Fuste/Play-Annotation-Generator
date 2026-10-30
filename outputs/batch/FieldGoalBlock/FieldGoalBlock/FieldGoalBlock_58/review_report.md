# Play-Annotation-Generator Annotation Review — FieldGoalBlock_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_58`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `0` | `0` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockKick` | FG_Block_Support1 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `0` | `0` | 23 | START | 23 | 41 |
| ✅ EXACT | `Action_KickBall` | Kicker | `4` | `4` | 49 | START | 49 | 51 |
| ✅ EXACT | `Action_BlockKick` | FG_Block_Support1 | `10` | `10` | 54 | START | 54 | 65 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PlaceBall` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_None` | 42 | 155 | 114 | inferred_complete_timeline |
| `Action_None` | 157 | 186 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_KickBall` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_None` | 52 | 208 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 153 | 105 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 156 | 108 | inferred_complete_timeline |
| `Action_None` | 176 | 198 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_None` | 73 | 151 | 79 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 159 | 111 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 143 | 95 | inferred_complete_timeline |
| `Action_None` | 150 | 209 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 79 | 31 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 132 | 166 | 35 | inferred_complete_timeline |
| `Action_None` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 196 | 8 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_BlockKick` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 194 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_None` | 49 | 67 | 19 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 174 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 100 | 52 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 112 | 64 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 6–12 | 7 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 23–90 | 68 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 27–28 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 59–200 | 136 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 74–138 | 37 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 74–101 | 25 | 4 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 82–99 | 16 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 87–121 | 35 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 94–116 | 17 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 119–181 | 61 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 120–210 | 86 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 120–123 | 4 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 130–175 | 42 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 133–159 | 27 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 143–210 | 59 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 150–210 | 61 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 173–210 | 32 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 179–199 | 21 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 184–197 | 14 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 81 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [42-155] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-186] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-196] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-156] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-198] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-174] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [54-65] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-143] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-159] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-151] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-93] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-121] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-168] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-159] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '36' has 1 frames without a visible bounding box.
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

</details>