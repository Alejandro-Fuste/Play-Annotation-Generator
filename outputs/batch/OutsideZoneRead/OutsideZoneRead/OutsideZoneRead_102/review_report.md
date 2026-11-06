# Play-Annotation-Generator Annotation Review — OutsideZoneRead_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_102`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 1 | START | 1 | 18 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 4 | START | 4 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 4 | START | 19 | 20 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 4 | START | 4 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 4 | START | 4 | 43 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 4 | START | 4 | 62 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 18 | END | 1 | 18 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `7` | `6` | 23 | START | 23 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `7` | `6` | 36 | START | 36 | 41 |
| ✅ EXACT | `Action_BallCarry` | QB | `7` | `6` | 45 | START | 45 | 45 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 62 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 18 | 18 | inferred_complete_timeline |
| `Action_None` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_Keep` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_Keep` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 45 | 45 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 32 | 32 | inferred_complete_timeline |
| `Action_None` | 38 | 95 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 54 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 18 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 77 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 43 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 59 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 61 | 61 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 68 | 116 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 29 | 29 | inferred_complete_timeline |
| `Action_None` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_None` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 60 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 107 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 41 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 66 | 66 | inferred_complete_timeline |
| `Action_None` | 77 | 87 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |
| `Action_None` | 76 | 139 | 64 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 5–71 | 66 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 45–180 | 136 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 46–179 | 134 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 52–67 | 16 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 101–111 | 11 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 111–180 | 66 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 119–180 | 62 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 121–180 | 60 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 170–180 | 7 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [1–18], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=19.
- ⚠️ Action 'Action_None' range [1-41] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-29] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-40] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-49] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-139] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [36-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '6' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [45-45] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-43] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-54] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-32] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-116] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-67] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-111] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-151] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>