# Play-Annotation-Generator Annotation Review — FieldGoalBlock_121

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_121`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 180
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `4` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `9` | `9` | 13 | START | 13 | 21 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 35 | START | 35 | 40 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PlaceBall` | 13 | 21 | 9 | inferred_complete_timeline |
| `Action_None` | 22 | 107 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 150 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_KickBall` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_None` | 41 | 108 | 68 | inferred_complete_timeline |
| `Action_None` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 56 | 22 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 43 | 9 | inferred_complete_timeline |
| `Action_None` | 53 | 80 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_None` | 78 | 103 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 79 | 45 | inferred_complete_timeline |
| `Action_None` | 81 | 104 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 34 | 7 | inferred_complete_timeline |
| `Action_None` | 35 | 43 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 35 | 83 | 49 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 68 | 19 | inferred_complete_timeline |
| `Action_None` | 71 | 74 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 55 | 21 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 97 | 63 | inferred_complete_timeline |
| `Action_None` | 99 | 150 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 93 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 107 | 73 | inferred_complete_timeline |
| `Action_None` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 53 | 19 | inferred_complete_timeline |
| `Action_None` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_None` | 60 | 108 | 49 | inferred_complete_timeline |
| `Action_None` | 110 | 150 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 108 | 68 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 150 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 106 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_None` | 35 | 58 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–22 | 22 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 6–150 | 136 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 9–71 | 59 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 9–68 | 39 | 7 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 32–77 | 41 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 33–79 | 47 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 40–150 | 111 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 47–65 | 17 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 55–60 | 6 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 70–150 | 76 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 74–134 | 51 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 83–117 | 11 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 83–150 | 48 | 3 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 85–150 | 63 | 3 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 88–114 | 25 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 89–144 | 55 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 91–129 | 29 | 5 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 94–150 | 47 | 3 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 95–125 | 19 | 5 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 101–150 | 37 | 5 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 119–150 | 32 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 127–150 | 16 | 3 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 127–150 | 17 | 2 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 129–150 | 18 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 138–150 | 7 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BlockKick' at frame 40 targets track ID '-', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 126 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 243: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 244: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [35-106] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-55] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-56] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-79] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-104] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-83] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-80] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-40] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-103] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-108] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-68] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-22] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-150] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-66] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-16] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-40] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-60] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-60] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-104] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-122] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-109] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-109] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '32' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-109] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-139] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-109] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-150] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-141] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-142] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '43' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'FieldGoalBlock_121'; source metadata written as null.

</details>