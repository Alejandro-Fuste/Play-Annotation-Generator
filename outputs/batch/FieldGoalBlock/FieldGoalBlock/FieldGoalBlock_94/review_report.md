# Play-Annotation-Generator Annotation Review — FieldGoalBlock_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_94`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | FG_Block_Support2 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `8` | `8` | 5 | START | 5 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `3` | `3` | 24 | START | 24 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | FG_Block_Support2 | `7` | `7` | 29 | START | 29 | 29 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PlaceBall` | 5 | 15 | 11 | inferred_complete_timeline |
| `Action_None` | 16 | 120 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_KickBall` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_KickBall` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_None` | 30 | 120 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 20 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 108 | 60 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_None` | 24 | 40 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 98 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_None` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_None` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 32 | 5 | inferred_complete_timeline |
| `Action_None` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 120 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 107 | 15 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_None` | 39 | 59 | 21 | inferred_complete_timeline |
| `Action_None` | 64 | 120 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 93 | 70 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 120 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 24 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_BlockKick` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_BlockKick` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 24 | 29 | 6 | inferred_complete_timeline |
| `Action_None` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_None` | 51 | 65 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 120 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 40 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 3–120 | 118 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 8–99 | 92 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 14–120 | 65 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 16–103 | 88 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 45–120 | 43 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 47–120 | 67 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 88–120 | 33 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 89–120 | 32 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 91–102 | 6 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 98–120 | 23 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 108–111 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockKick` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_End` position mapped to `offense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 68 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [24-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' for track '3' starts at frame 24, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_KickBall' range [24-24] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [26-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 24, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [24-24] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-32] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-37] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-59] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-120] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-24] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' for track '7' starts at frame 29, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockKick' range [29-29] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [33-34] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-26] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-40] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-20] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-47] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 24, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [24-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-103] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-73] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-120] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-120] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '25' has 1 frames without a visible bounding box.
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

</details>