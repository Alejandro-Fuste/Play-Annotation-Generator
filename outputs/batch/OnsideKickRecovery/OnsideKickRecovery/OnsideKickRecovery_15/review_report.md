# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_AttemptRecovery` | Kick_Returner1 | defense | `0` | `0` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Coverage1 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `6` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `8` | `Group` | 0 | START | 0 | 1 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `12` | `12` | 2 | START | 2 | 24 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 43 | START | 43 | 45 |
| ✅ EXACT | `Action_AttemptRecovery` | Kick_Returner1 | `0` | `0` | 129 | START | 129 | 148 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Coverage1 | `6` | `6` | 157 | START | 157 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 24 | 23 | inferred_complete_timeline |
| `Action_KickApproach` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_KickBall` | 43 | 45 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 144 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_SecureRecovery` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 62 | 61 | inferred_complete_timeline |
| `Action_None` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_None` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 113 | 18 | inferred_complete_timeline |
| `Action_None` | 115 | 145 | 31 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 167 | 10 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 35 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 114 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_None` | 21 | 28 | 8 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 121 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 80 | 79 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 191 | 88 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 129 | 148 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 78 | 77 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 30 | 29 | inferred_complete_timeline |
| `Action_None` | 32 | 83 | 52 | inferred_complete_timeline |
| `Action_None` | 97 | 103 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 5 | 4 | inferred_complete_timeline |
| `Action_None` | 10 | 124 | 115 | inferred_complete_timeline |
| `Action_None` | 127 | 156 | 30 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 115 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 126 | 125 | inferred_complete_timeline |
| `Action_None` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 163 | 195 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 201 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 75 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 137 | 61 | inferred_complete_timeline |
| `Action_None` | 139 | 210 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–208 | 83 | 15 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 7–13 | 7 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 43–204 | 162 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 46–210 | 148 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 53–210 | 158 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 53–54 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 60–210 | 145 | 3 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 60–198 | 123 | 4 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 69–98 | 26 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 120–124 | 5 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 121–210 | 90 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 138–210 | 63 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 146–210 | 50 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 155–210 | 48 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 162–210 | 49 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 168–173 | 6 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 176–210 | 27 | 3 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 188–210 | 16 | 3 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 192–208 | 17 | 1 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 198–209 | 12 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Support6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kick_Returner4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kick_Returner3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 32: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_AttemptRecovery' range [129-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-80] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-144] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [157-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-62] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-84] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-30] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-83] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [2-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [26-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [43-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-114] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-156] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-14] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-15] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-13] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-204] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-70] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-100] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-152] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-154] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-73] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-130] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-178] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-187] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-208] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>