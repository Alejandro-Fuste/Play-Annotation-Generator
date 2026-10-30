# Play-Annotation-Generator Annotation Review — FieldGoalBlock_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_8`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `6` | `6` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `3` | `3` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher2 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `3` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `4` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `6` | `6` | 4 | START | 4 | 20 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `3` | `3` | 21 | START | 21 | 34 |
| ✅ EXACT | `Action_KickBall` | Kicker | `4` | `4` | 40 | START | 40 | 45 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher2 | `8` | `8` | 46 | START | 46 | 54 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PlaceBall` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 74 | 40 | inferred_complete_timeline |
| `Action_None` | 78 | 112 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_KickBall` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_None` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_None` | 61 | 128 | 68 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_None` | 32 | 58 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 4 | 10 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 66 | 76 | 11 | inferred_complete_timeline |
| `Action_None` | 79 | 102 | 24 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_None` | 69 | 239 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_LongSnap` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_None` | 21 | 101 | 81 | inferred_complete_timeline |
| `Action_None` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 139 | 208 | 70 | inferred_complete_timeline |
| `Action_None` | 213 | 218 | 6 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 27 | 24 | inferred_complete_timeline |
| `Action_None` | 67 | 123 | 57 | inferred_complete_timeline |
| `Action_None` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_None` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 223 | 165 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 74 | 71 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 119 | 29 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 239 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_None` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_None` | 46 | 83 | 38 | inferred_complete_timeline |
| `Action_None` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 97 | 94 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 109 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 146 | 29 | inferred_complete_timeline |
| `Action_None` | 148 | 224 | 77 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BlockKick` | 46 | 54 | 9 | inferred_complete_timeline |
| `Action_None` | 55 | 239 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 7 | 4 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 99 | 39 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 32 | 29 | inferred_complete_timeline |
| `Action_None` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_None` | 46 | 61 | 16 | inferred_complete_timeline |
| `Action_None` | 67 | 100 | 34 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 90 | 87 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 4–239 | 224 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 14–239 | 215 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–239 | 185 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 114–235 | 103 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 132–197 | 66 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 134–239 | 106 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 152–239 | 88 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 161–170 | 7 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 83 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-38] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-146] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-224] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-59] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-208] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-223] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-74] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-61] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-123] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-83] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-7] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-64] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-165] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-190] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-231] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '29' has 1 frames without a visible bounding box.
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