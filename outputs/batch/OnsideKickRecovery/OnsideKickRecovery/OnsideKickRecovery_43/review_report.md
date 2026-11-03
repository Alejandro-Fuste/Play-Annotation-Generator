# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Onside_Recovery_Front4 | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `11` | `11` | 2 | START | 2 | 40 |
| ✅ EXACT | `Action_KickBall` | Kicker | `11` | `11` | 41 | START | 41 | 73 |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Onside_Recovery_Front4 | `4` | `4` | 107 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_KickBall` | 41 | 73 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 117 | 116 | inferred_complete_timeline |
| `Action_None` | 119 | 167 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 4 | 3 | inferred_complete_timeline |
| `Action_None` | 8 | 50 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 93 | 92 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 159 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 91 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 93 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 127 | 126 | inferred_complete_timeline |
| `Action_None` | 131 | 145 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 4 | 3 | inferred_complete_timeline |
| `Action_None` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 42 | 17 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 180 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 147 | 146 | inferred_complete_timeline |
| `Action_None` | 149 | 180 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 135 | 134 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 78 | 77 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 27 | 26 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 103 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 143 | 142 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 147 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `10`</summary>

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
<summary>Onside_Recovery_Support2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 121 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 80 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 113 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `0`</summary>

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

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 8–66 | 53 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 36–180 | 145 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 56–180 | 125 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 58–180 | 121 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 64–83 | 20 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 70–93 | 7 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 72–73 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 77–158 | 64 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 88–180 | 73 | 8 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 154–158 | 5 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 156–180 | 23 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_AttemptRecovery` on target `4` (Onside_Recovery_Front4)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_AttemptRecovery' for track '4' has invalid range: start=107, end=103. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-143] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-135] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-78] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [41-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-93] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-27] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-147] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-42] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-59] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-73] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-95] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-131] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-144] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '31' has 2 frames without a visible bounding box.
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

</details>