# Play-Annotation-Generator Annotation Review — CrackToss_98

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_98`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 134
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `3` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 21 | START | 21 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `21` | `19` | 24 | START | 28 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR1 | `1` | `0` | 24 | START | 24 | 65 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 30 | END | 21 | 30 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 30 | 10 | inferred_complete_timeline |
| `Action_None` | 31 | 150 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 123 | 103 | inferred_complete_timeline |
| `Action_None` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 5 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 24 | 127 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 24 | 65 | 42 | inferred_complete_timeline |
| `Action_PullBlock` | 68 | 72 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 5 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 67 | 42 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_None` | 28 | 61 | 34 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 150 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_None` | 24 | 60 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 13 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 30 | 10 | inferred_complete_timeline |
| `Action_None` | 31 | 69 | 39 | inferred_complete_timeline |
| `Action_None` | 71 | 150 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 65 | 40 | inferred_complete_timeline |
| `Action_None` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_None` | 27 | 35 | 9 | inferred_complete_timeline |
| `Action_None` | 37 | 61 | 25 | inferred_complete_timeline |
| `Action_None` | 94 | 150 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_None` | 28 | 41 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 132 | 112 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 76 | 56 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 116 | 31 | inferred_complete_timeline |
| `Action_None` | 118 | 150 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 67 | 47 | inferred_complete_timeline |
| `Action_None` | 77 | 150 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 53 | 33 | inferred_complete_timeline |
| `Action_None` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 62 | 127 | 66 | inferred_complete_timeline |
| `Action_None` | 129 | 150 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 67 | 47 | inferred_complete_timeline |
| `Action_None` | 69 | 143 | 75 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 150 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–14 | 15 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 25–150 | 126 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 28–150 | 81 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 29–150 | 73 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 29–59 | 28 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 37–150 | 89 | 11 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 87–111 | 18 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 89–90 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 90–150 | 49 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 95–143 | 49 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 101–111 | 5 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 119–150 | 29 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 121–150 | 30 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 144–149 | 6 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 98, Column 'Toss': Unknown/missing frame number '' in entry ',5'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 103 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PullBlock' range [24-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [68-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-53] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-127] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-67] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-150] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-150] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 21, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [21-21] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-127] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-76] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-67] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-67] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-60] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-41] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-61] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [21-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 31, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [31-69] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-150] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [28-63] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [87-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [100-111] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [120-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [126-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [133-137] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [141-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-50] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-150] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-33] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-112] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-105] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-143] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-129] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>