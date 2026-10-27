# Play-Annotation-Generator Annotation Review — CrackToss_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_82`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | DT1 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `6` | `5` | 66 | START | 66 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR | `3` | `2` | 69 | START | 69 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | DT1 | `5` | `4` | 69 | START | 69 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `12` | `11` | 69 | START | 69 | 136 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `18` | `17` | 69 | START | 69 | 144 |
| ✅ EXACT | `Action_SnapReceive` | LT | `9` | `8` | 75 | END | 66 | 75 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 79 | START | 79 | 96 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 97 | START | 97 | 124 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_Toss` | 79 | 96 | 18 | inferred_complete_timeline |
| `Action_None` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 131 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 124 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_CrackBlock` | 69 | 92 | 24 | inferred_complete_timeline |
| `Action_CrackBlock` | 95 | 103 | 9 | inferred_complete_timeline |
| `Action_CrackBlock` | 118 | 144 | 27 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 144 | 76 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 146 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SnapReceive` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 93 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_None` | 105 | 150 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_None` | 66 | 95 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 65 | 56 | inferred_complete_timeline |
| `Action_None` | 66 | 144 | 79 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 136 | 68 | inferred_complete_timeline |
| `Action_PullBlock` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 115 | 50 | inferred_complete_timeline |
| `Action_None` | 117 | 142 | 26 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_CrackBlock` | 69 | 113 | 45 | inferred_complete_timeline |
| `Action_CrackBlock` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_CrackBlock` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 65 | 62 | inferred_complete_timeline |
| `Action_None` | 66 | 119 | 54 | inferred_complete_timeline |
| `Action_None` | 122 | 150 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 108 | 43 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 150 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 65 | 56 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 122 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 65 | 53 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–150 | 151 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–150 | 151 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–150 | 133 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–35 | 32 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 5–29 | 21 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 53–76 | 23 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 67–71 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 111–150 | 31 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 166: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 166: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [66-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-146] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [69-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [95-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [118-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [69-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [126-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [134-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-115] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [69-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [142-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-29] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 66, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [66-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>