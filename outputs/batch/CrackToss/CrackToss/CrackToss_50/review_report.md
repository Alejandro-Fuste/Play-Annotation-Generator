# Play-Annotation-Generator Annotation Review — CrackToss_50

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_50`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 73
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE | offense | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 15 | START | 15 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 15 | START | 15 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 15 | START | 15 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 15 | START | 15 | 18 |
| ✅ EXACT | `Action_BallSnap` | RG | `20` | `19` | 19 | START | 19 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE | `17` | `16` | 22 | START | 22 | 23 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `19` | 22 | START | 22 | 23 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 30 | END | 19 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `16` | `15` | 33 | START | 33 | 33 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 51 | START | 51 | 92 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–125
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_Toss` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_Toss` | 35 | 50 | 16 | inferred_complete_timeline |
| `Action_None` | 51 | 125 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–92
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 50 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 92 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–125
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 125 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 15–106
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_None` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 106 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–47
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 47 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 15–125
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_CrackBlock` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 108 | 125 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 15–31
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 31 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–23
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–30
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 30 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–23
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 22 | 23 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 15–19
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 19 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 15–125
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 39 | 21 | inferred_complete_timeline |
| `Action_None` | 43 | 107 | 65 | inferred_complete_timeline |
| `Action_None` | 110 | 125 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–31
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 15–125
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 72 | 125 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–23
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–118
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 107 | 89 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–60
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 60 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–125
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 125 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–125
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 39 | 21 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 125 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–106
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 100 | 82 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–125
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 125 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–95
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 95 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 50–81 | 32 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 79–125 | 45 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 81–125 | 36 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 84–120 | 37 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 86–125 | 40 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 96–125 | 29 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 113–124 | 10 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 114–125 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 80 targets track ID '93', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [19-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-107] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-125] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-100] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-31] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-92] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' for track '15' starts at frame 33, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Toss' range [33-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [35-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [22-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [108-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [19-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [22-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 19, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [19-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-108] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-125] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-125] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '29' has 2 frames without a visible bounding box.
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