# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_28`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Position_Unknown | Team_Unknown | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 7 | START | 7 | 49 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 50 | START | 50 | 180 |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Position_Unknown | `19` | `19` | 106 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | `19` | `19` | 112 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_KickApproach` | 7 | 49 | 43 | inferred_complete_timeline |
| `Action_KickBall` | 50 | 180 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 28 | 22 | inferred_complete_timeline |
| `Action_None` | 36 | 180 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 119 | 113 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 152 | 16 | inferred_complete_timeline |
| `Action_None` | 155 | 180 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 95 | 89 | inferred_complete_timeline |
| `Action_None` | 98 | 135 | 38 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 34 | 83 | 50 | inferred_complete_timeline |
| `Action_None` | 86 | 116 | 31 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_None` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_None` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_None` | 25 | 50 | 26 | inferred_complete_timeline |
| `Action_None` | 52 | 66 | 15 | inferred_complete_timeline |
| `Action_None` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_None` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 110 | 15 | inferred_complete_timeline |
| `Action_None` | 128 | 141 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 47 | 41 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_None` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 111 | 170 | 60 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 137 | 131 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 153 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 180 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front8 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 125 | 119 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 3–58 | 42 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 4–46 | 17 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 8–92 | 26 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 35–146 | 89 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 39–91 | 53 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 56–104 | 44 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 79–180 | 100 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 97–180 | 71 | 8 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 105–180 | 44 | 10 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 169–180 | 12 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 172–180 | 9 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_AttemptRecovery` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureRecovery` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front8` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_AttemptRecovery' for track '19' has invalid range: start=106, end=46. Clamping end to start.
- ⚠️ Segment 'Action_SecureRecovery' for track '19' has invalid range: start=112, end=46. Clamping end to start.
- ⚠️ Action 'Action_None' range [7-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-95] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-180] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-31] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-83] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [50-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-119] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-19] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-50] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-66] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-32] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-46] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
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

</details>