# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_30`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 114
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
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage5 | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Left_Coverage5 | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Kicker | offense | `6` | `6` |
| ✅ EXACT | `Action_SecureRecovery` | Kicker | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage5 | `12` | `12` | 10 | START | 10 | 39 |
| ✅ EXACT | `Action_KickBall` | Left_Coverage5 | `12` | `12` | 40 | START | 40 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Kicker | `6` | `6` | 96 | START | 96 | 98 |
| ✅ EXACT | `Action_SecureRecovery` | Kicker | `6` | `6` | 109 | START | 109 | 115 |

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
- **Visible Frames:** 0–115
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_SecureRecovery` | 109 | 115 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 58 | 49 | inferred_complete_timeline |
| `Action_None` | 60 | 95 | 36 | inferred_complete_timeline |
| `Action_None` | 97 | 126 | 30 | inferred_complete_timeline |
| `Action_None` | 128 | 150 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 88 | 79 | inferred_complete_timeline |
| `Action_None` | 91 | 128 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 55 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_KickApproach` | 10 | 39 | 30 | inferred_complete_timeline |
| `Action_KickBall` | 40 | 128 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 50 | 101 | 52 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 29 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 81 | 34 | inferred_complete_timeline |
| `Action_None` | 119 | 130 | 12 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 86 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_None` | 100 | 150 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 132 | 123 | inferred_complete_timeline |
| `Action_None` | 137 | 144 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 85 | 76 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 79 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 128 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 93 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 21–97 | 66 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 52–90 | 37 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 56–128 | 71 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 58–109 | 26 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 62–150 | 87 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 68–86 | 19 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 71–75 | 5 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 99–128 | 30 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 106–150 | 42 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 120–150 | 31 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 129–148 | 20 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 129–132 | 4 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 129–150 | 22 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 129–150 | 22 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 133–138 | 6 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 137–150 | 13 | 2 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 142–146 | 5 | 1 | Undefined position; Undefined team |
| `36` | `38` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `37` | `39` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 71 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-132] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [96-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [109-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-79] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [40-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '37' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>