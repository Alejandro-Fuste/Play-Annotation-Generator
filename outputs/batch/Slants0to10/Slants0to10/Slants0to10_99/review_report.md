# Play-Annotation-Generator Annotation Review — Slants0to10_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `15` | `15` | 7 | START | 7 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 7 | START | 7 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 7 | START | 7 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 7 | START | 7 | 28 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 7 | START | 7 | 75 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `4` | `4` | 15 | START | 15 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 15 | END | 15 | 15 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 59 | START | 59 | 67 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `4` | `4` | 96 | START | 96 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_None` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 67 | 9 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 180 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 119 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 180 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 180 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 180 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 126 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 168 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 75 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 28 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 35 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 63 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 73 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 78 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 83 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 74 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 180 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 121 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 140 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 166 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 145 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 157 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 144 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 164 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 126 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 127 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 180 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 96 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 105 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 23–25 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 36–137 | 13 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 82–179 | 48 | 8 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 106–180 | 75 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 112–115 | 4 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 121–180 | 59 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 123–176 | 47 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 128–180 | 53 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 128–180 | 44 | 4 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 144–180 | 37 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 145–180 | 23 | 4 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 165–180 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 107 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-140] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-126] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-127] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [59-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-74] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-73] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-78] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-145] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-157] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-28] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-39] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-121] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-180] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-139] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-148] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-170] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>