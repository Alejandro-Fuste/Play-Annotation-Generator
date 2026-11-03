# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_AttemptRecovery` | Kicker | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Kicker | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 4 | START | 4 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `8` | `8` | 75 | START | 75 | 101 |
| ⚠️ START CHANGED | `Action_AttemptRecovery` | Kicker | `8` | `8` | 132 | START | 143 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Kicker | `8` | `8` | 145 | START | 145 | 150 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_KickApproach` | 4 | 74 | 71 | inferred_complete_timeline |
| `Action_KickBall` | 75 | 101 | 27 | inferred_complete_timeline |
| `Action_KickBall` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_KickBall` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_KickBall` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_KickBall` | 125 | 130 | 6 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_SecureRecovery` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_SecureRecovery` | 153 | 174 | 22 | inferred_complete_timeline |
| `Action_SecureRecovery` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 163 | 160 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 97 | 94 | inferred_complete_timeline |
| `Action_None` | 104 | 109 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 130 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 84 | 81 | inferred_complete_timeline |
| `Action_None` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 130 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 82 | 79 | inferred_complete_timeline |
| `Action_None` | 89 | 105 | 17 | inferred_complete_timeline |
| `Action_None` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_None` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 32 | 180 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 50 | 47 | inferred_complete_timeline |
| `Action_None` | 55 | 180 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 134 | 131 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 136 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 14–180 | 153 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 95–180 | 84 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 116–131 | 14 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 120–180 | 61 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 125–130 | 6 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 167–171 | 5 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `8` (5 segments found)
- ⚠️ `Action_AttemptRecovery` for actor_track_id `8` (Kicker): Annotated start 132 != Inferred start 143
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-97] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-163] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-136] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [75-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [107-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [110-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [115-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [125-130] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [145-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [153-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [179-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-50] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-180] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-180] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-82] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-105] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-22] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-136] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
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

</details>