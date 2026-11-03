# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Kicker | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `3` | `3` | 2 | START | 2 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `3` | `3` | 29 | START | 29 | 64 |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | `3` | `3` | 84 | START | 84 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Kicker | `3` | `3` | 91 | START | 91 | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_KickBall` | 29 | 64 | 36 | inferred_complete_timeline |
| `Action_KickBall` | 66 | 83 | 18 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_SecureRecovery` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_SecureRecovery` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_SecureRecovery` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_SecureRecovery` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_SecureRecovery` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_SecureRecovery` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_SecureRecovery` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 170 | 169 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 117 | 116 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 87 | 86 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 9 | 8 | inferred_complete_timeline |
| `Action_None` | 12 | 107 | 96 | inferred_complete_timeline |
| `Action_None` | 109 | 128 | 20 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 175 | 25 | inferred_complete_timeline |
| `Action_None` | 178 | 196 | 19 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 192 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 9 | 8 | inferred_complete_timeline |
| `Action_None` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_None` | 27 | 127 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_None` | 59 | 133 | 75 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `9`</summary>

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

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 89 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_None` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_None` | 11 | 99 | 89 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 101 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 198 | 197 | inferred_complete_timeline |
| `Action_None` | 201 | 208 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 13–210 | 198 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 31–32 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 50–210 | 156 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 69–209 | 141 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 69–210 | 142 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 73–210 | 132 | 5 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 100–210 | 103 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 105–210 | 101 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 118–134 | 12 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 141–174 | 21 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 154–210 | 43 | 6 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 172–210 | 29 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 172–210 | 32 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `3` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 89 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [2-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-170] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [29-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [91-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [102-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [117-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [129-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [135-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [143-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [152-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-107] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-117] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-99] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-133] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-127] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-209] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-133] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>