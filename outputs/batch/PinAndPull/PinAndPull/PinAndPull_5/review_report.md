# Play-Annotation-Generator Annotation Review — PinAndPull_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_5`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_BallSnap` | RG | `21` | `20` | 49 | START | 49 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 52 | START | 60 | 67 |
| ✅ EXACT | `Action_PullBlock` | LT | `18` | `17` | 52 | START | 52 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `17` | `16` | 52 | START | 52 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 63 | END | 49 | 63 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 73 | START | 73 | 106 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 124 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_None` | 64 | 72 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 106 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 58 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 83 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 200 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 200 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 74 | 26 | inferred_complete_timeline |
| `Action_None` | 110 | 149 | 40 | inferred_complete_timeline |
| `Action_None` | 178 | 200 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 79 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 84 | 19 | inferred_complete_timeline |
| `Action_None` | 88 | 150 | 63 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 200 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_None` | 65 | 98 | 34 | inferred_complete_timeline |
| `Action_None` | 101 | 200 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 103 | 52 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_None` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_None` | 113 | 137 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 113 | 65 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 200 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 103 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 69 | 21 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 87 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_None` | 70 | 118 | 49 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 200 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 200 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 150 | 102 | inferred_complete_timeline |
| `Action_None` | 152 | 176 | 25 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 200 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 93 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–124 | 125 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–109 | 75 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 60–200 | 130 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 66–200 | 135 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 89–200 | 103 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 106–156 | 45 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 116–173 | 53 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 130–200 | 58 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 138–152 | 15 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 160–200 | 41 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 164–179 | 11 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 168–200 | 29 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 169–173 | 5 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 188–191 | 4 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 192–200 | 9 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 195–200 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 73 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [49-200] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-124] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-84] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-150] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-69] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-176] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-200] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-137] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [52-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [52-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-118] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [49-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-98] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-163] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-182] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-191] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>