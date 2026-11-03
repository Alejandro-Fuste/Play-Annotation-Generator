# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_37`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureRecovery` | Kicker | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `10` | `10` | 1 | START | 1 | 85 |
| ✅ EXACT | `Action_KickBall` | Kicker | `10` | `10` | 86 | START | 86 | 131 |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | `10` | `10` | 132 | START | 132 | 141 |
| ✅ EXACT | `Action_SecureRecovery` | Kicker | `10` | `10` | 142 | START | 142 | 146 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_KickApproach` | 1 | 85 | 85 | inferred_complete_timeline |
| `Action_KickBall` | 86 | 131 | 46 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_SecureRecovery` | 142 | 146 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 168 | 168 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 170 | 170 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 144 | 144 | inferred_complete_timeline |
| `Action_None` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 142 | 142 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 132 | 132 | inferred_complete_timeline |
| `Action_None` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 147 | 147 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 73 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_None` | 84 | 161 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 122 | 122 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 170 | 170 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 166 | 166 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 136 | 136 | inferred_complete_timeline |
| `Action_None` | 146 | 163 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 119 | 119 | inferred_complete_timeline |
| `Action_None` | 122 | 180 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 54–71 | 6 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 79–180 | 101 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 88–178 | 83 | 7 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 97–178 | 72 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 100–178 | 50 | 7 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 112–144 | 33 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 114–180 | 67 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 116–180 | 61 | 4 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 117–180 | 63 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 117–180 | 63 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 132–149 | 18 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 146–170 | 25 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 166–180 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [1-170] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [142-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-144] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-149] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>