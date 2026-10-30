# Play-Annotation-Generator Annotation Review — FieldGoalBlock_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_77`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockKick` | Right_Edge_Rusher | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `16` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 7 | START | 7 | 29 |
| ✅ EXACT | `Action_KickBall` | Kicker | `4` | `4` | 48 | START | 48 | 55 |
| ✅ EXACT | `Action_BlockKick` | Right_Edge_Rusher | `10` | `10` | 51 | START | 51 | 72 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PlaceBall` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 46 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_KickBall` | 48 | 55 | 8 | inferred_complete_timeline |
| `Action_None` | 56 | 182 | 127 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 47 | 14 | inferred_complete_timeline |
| `Action_None` | 48 | 63 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 156 | 109 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 181 | 234 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 46 | 6 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 58 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 97 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_None` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_None` | 80 | 128 | 49 | inferred_complete_timeline |
| `Action_None` | 137 | 185 | 49 | inferred_complete_timeline |
| `Action_None` | 203 | 228 | 26 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 184 | 137 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 61 | 104 | 44 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 174 | 66 | inferred_complete_timeline |
| `Action_None` | 187 | 218 | 32 | inferred_complete_timeline |
| `Action_None` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–11
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 47 | 22 | inferred_complete_timeline |
| `Action_None` | 48 | 65 | 18 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 96 | 27 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 29 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 150 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BlockKick` | 51 | 72 | 22 | inferred_complete_timeline |
| `Action_None` | 73 | 151 | 79 | inferred_complete_timeline |
| `Action_None` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 7–136 | 130 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 9–32 | 21 | 2 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 56–239 | 144 | 6 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 57–239 | 175 | 4 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 61–113 | 45 | 3 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 65–239 | 175 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 72–125 | 54 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 76–81 | 4 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 78–233 | 148 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 97–118 | 8 | 2 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 102–144 | 42 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 103–203 | 92 | 2 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 112–239 | 127 | 2 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 120–239 | 120 | 1 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 131–239 | 67 | 3 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 135–137 | 3 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 147–239 | 51 | 5 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 147–173 | 26 | 2 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 156–175 | 18 | 2 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 180–239 | 50 | 3 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 187–202 | 13 | 2 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 196–237 | 15 | 3 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 103 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [48-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-96] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-46] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-184] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-29] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-151] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-97] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-128] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-32] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-170] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-68] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-84] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-140] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-203] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-159] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-168] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-224] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>