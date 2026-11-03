# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_16`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Right_Coverage2 | offense | `8` | `8` |
| ✅ EXACT | `Action_AttemptRecovery` | Position_Unknown | Team_Unknown | `29` | `25` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `21` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 1 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `6` | `6` | 2 | START | 2 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Right_Coverage2 | `8` | `8` | 61 | START | 61 | 143 |
| ✅ EXACT | `Action_AttemptRecovery` | Position_Unknown | `29` | `25` | 129 | START | 129 | 157 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | `21` | `19` | 137 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 41 | 40 | inferred_complete_timeline |
| `Action_KickApproach` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_KickApproach` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_KickApproach` | 98 | 117 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 162 | 161 | inferred_complete_timeline |
| `Action_None` | 165 | 180 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 43 | 42 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_None` | 153 | 180 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 130 | 129 | inferred_complete_timeline |
| `Action_None` | 132 | 180 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 140 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 60 | 27 | inferred_complete_timeline |
| `Action_KickBall` | 61 | 143 | 83 | inferred_complete_timeline |
| `Action_KickBall` | 145 | 160 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 24 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_None` | 74 | 180 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 41 | 40 | inferred_complete_timeline |
| `Action_None` | 45 | 70 | 26 | inferred_complete_timeline |
| `Action_None` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_None` | 88 | 121 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 103 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 89 | 88 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 156 | 27 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 163 | 162 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 104 | 103 | inferred_complete_timeline |
| `Action_None` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 164 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 23 | 22 | inferred_complete_timeline |
| `Action_None` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_None` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_None` | 51 | 57 | 7 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 97 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 127 | 126 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–116 | 38 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 28–135 | 58 | 8 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 28–99 | 42 | 8 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 45–46 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 56–58 | 3 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 59–136 | 56 | 7 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 65–123 | 59 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 69–101 | 33 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 76–157 | 82 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 82–88 | 5 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 129–132 | 4 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 137–176 | 30 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 143–180 | 38 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 148–164 | 17 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 169–179 | 11 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `6` (6 segments found)
- ⚠️ Ambiguous match for action `Action_KickBall` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `21` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '19' has invalid range: start=137, end=99. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-41] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-86] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-127] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-122] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [2-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [44-46] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [51-63] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [68-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [83-90] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [98-117] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [61-143] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [145-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-24] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-180] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-89] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-156] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-140] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-43] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-151] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-43] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-92] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-110] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [129-157] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-164] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '33' has 1 frames without a visible bounding box.
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

</details>