# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 139
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_KickBall` | Kicker | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Kicker | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `14` | `14` | 3 | START | 3 | 15 |
| ⚠️ START CHANGED | `Action_KickBall` | Kicker | `14` | `14` | 34 | START | 55 | 62 |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Kicker | `14` | `14` | 93 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | `14` | `14` | 99 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 3 | 15 | 13 | inferred_complete_timeline |
| `Action_KickBall` | 55 | 62 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_None` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_None` | 19 | 24 | 6 | inferred_complete_timeline |
| `Action_None` | 26 | 93 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 42 | 40 | inferred_complete_timeline |
| `Action_None` | 45 | 110 | 66 | inferred_complete_timeline |
| `Action_None` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 162 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 74 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 90 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 95 | 93 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 21 | 19 | inferred_complete_timeline |
| `Action_None` | 24 | 59 | 36 | inferred_complete_timeline |
| `Action_None` | 66 | 97 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 66 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 164 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 94 | 92 | inferred_complete_timeline |
| `Action_None` | 102 | 147 | 46 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 96 | 94 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 177 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 80 | 78 | inferred_complete_timeline |
| `Action_None` | 88 | 93 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 77 | 75 | inferred_complete_timeline |
| `Action_None` | 80 | 116 | 37 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 128 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 131 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_None` | 13 | 111 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_None` | 5 | 14 | 10 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 148 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 6–123 | 96 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 16–170 | 138 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 28–132 | 99 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 34–36 | 3 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–180 | 137 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 49–112 | 31 | 7 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 75–128 | 54 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 80–83 | 4 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 81–108 | 26 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 117–180 | 39 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 124–159 | 24 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 155–162 | 8 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 155–164 | 10 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 156–177 | 17 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 157–180 | 24 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 171–180 | 10 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 172–180 | 6 | 2 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 174–180 | 7 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_KickBall` for actor_track_id `14` (Kicker): Annotated start 34 != Inferred start 55
- ❌ Missing segment for action `Action_AttemptRecovery` on target `14` (Kicker)
- ❌ Missing segment for action `Action_SecureRecovery` on target `14` (Kicker)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_AttemptRecovery' for track '14' has invalid range: start=93, end=62. Clamping end to start.
- ⚠️ Segment 'Action_SecureRecovery' for track '14' has invalid range: start=99, end=62. Clamping end to start.
- ⚠️ Action 'Action_None' range [3-94] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-147] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-164] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-96] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-42] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-110] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-21] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-59] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-111] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [3-15] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [55-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 3, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [3-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-24] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 3, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [3-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-14] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-106] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-99] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>