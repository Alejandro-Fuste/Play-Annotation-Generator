# Play-Annotation-Generator Annotation Review — SplitZone_179

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_179`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 91
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 10 | START | 20 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 10 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 10 | START | 20 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 10 | START | 20 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `2` | `Group` | 10 | START | 20 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 10 | START | 20 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 10 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 10 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 10 | START | 20 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 10 | START | 20 | 45 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 46 | START | 46 | 59 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 49 | START | 60 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 49 | START | 49 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `17` | 49 | START | 49 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 49 | START | 49 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 49 | START | 49 | 107 |
| ✅ EXACT | `Action_SplitBlock` | HB | `2` | `2` | 53 | START | 53 | 129 |
| ✅ EXACT | `Action_SnapReceive` | RB | `7` | `7` | 59 | END | 46 | 59 |
| ✅ EXACT | `Action_Handoff` | RB | `7` | `7` | 62 | START | 62 | 70 |
| ✅ EXACT | `Action_BallCarry` | QB | `13` | `13` | 71 | START | 71 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 70 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 53 | 129 | 77 | inferred_complete_timeline |
| `Action_None` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–71
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 71 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–115
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 87 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–180
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 130 | 151 | 22 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 180 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–84
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 84 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 20–124
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 107 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 124 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 87 | 42 | inferred_complete_timeline |
| `Action_None` | 91 | 180 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 96 | 51 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 163 | 22 | inferred_complete_timeline |
| `Action_None` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–87
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 87 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 77 | 32 | inferred_complete_timeline |
| `Action_None` | 81 | 117 | 37 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 172 | 14 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 29 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 45 | 11 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 134 | 89 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 119 | 142 | 24 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 166 | 121 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 20–65 | 46 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 75–180 | 106 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 84–151 | 25 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 89–177 | 87 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 100–110 | 9 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 132–180 | 47 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `27` | 88 | 90 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 49 != Inferred start 60
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [46–59], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=60.
- ⚠️ Action 'Action_None' range [46-96] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-166] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-134] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-117] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-152] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
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