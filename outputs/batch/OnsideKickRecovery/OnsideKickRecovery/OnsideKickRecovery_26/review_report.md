# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 126
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
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Onside_Recovery_Front5 | defense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Onside_Recovery_Front5 | defense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Right_Coverage4 | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage4 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `17` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_KickApproach` | Onside_Recovery_Front5 | `2` | `2` | 3 | START | 3 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Onside_Recovery_Front5 | `2` | `2` | 50 | START | 50 | 94 |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Right_Coverage4 | `17` | `17` | 94 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage4 | `17` | `17` | 102 | START | N/A | N/A |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 161 | 159 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 62 | 60 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 55 | 53 | inferred_complete_timeline |
| `Action_None` | 57 | 92 | 36 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 127 | 24 | inferred_complete_timeline |
| `Action_None` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 141 | 180 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 64 | 62 | inferred_complete_timeline |
| `Action_None` | 66 | 96 | 31 | inferred_complete_timeline |
| `Action_None` | 99 | 143 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 24 | 22 | inferred_complete_timeline |
| `Action_None` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_None` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 180 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 50 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 85 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 92 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 71 | 27 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 169 | 167 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 3 | 49 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 50 | 94 | 45 | inferred_complete_timeline |
| `Action_KickBall` | 96 | 180 | 85 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front8 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 140 | 138 | inferred_complete_timeline |
| `Action_None` | 146 | 160 | 15 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 121 | 119 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 5–27 | 14 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 6–88 | 69 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 7–180 | 148 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 25–71 | 44 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 31–180 | 148 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 57–66 | 8 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 85–139 | 49 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 91–180 | 87 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 98–135 | 22 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 101–138 | 28 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 112–115 | 4 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 114–121 | 4 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 127–131 | 5 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 152–180 | 29 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_AttemptRecovery` on target `17` (Right_Coverage4)
- ❌ Missing segment for action `Action_SecureRecovery` on target `17` (Right_Coverage4)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front8` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_AttemptRecovery' for track '17' has invalid range: start=94, end=92. Clamping end to start.
- ⚠️ Segment 'Action_SecureRecovery' for track '17' has invalid range: start=102, end=92. Clamping end to start.
- ⚠️ Action 'Action_None' range [3-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [50-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [96-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-143] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-127] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-85] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-66] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-17] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-105] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-34] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-99] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-116] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-129] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
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

</details>