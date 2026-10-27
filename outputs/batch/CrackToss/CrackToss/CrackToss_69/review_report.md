# Play-Annotation-Generator Annotation Review — CrackToss_69

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 90
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `28` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | WR1 | offense | `28` | `27` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `23` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `25` | `24` |
| ✅ EXACT | `Action_Toss` | QB | offense | `25` | `24` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `20` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 3 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 3 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 3 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 3 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 3 | START | 3 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 3 | START | 3 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `23` | `Group` | 3 | START | 3 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `25` | `Group` | 3 | START | 3 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `26` | `Group` | 3 | START | 3 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `28` | `Group` | 3 | START | 3 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 18 | START | 18 | 27 |
| ✅ EXACT | `Action_CrackBlock` | WR1 | `28` | `27` | 21 | START | 21 | 150 |
| ✅ EXACT | `Action_PullBlock` | RT | `23` | `22` | 21 | START | 21 | 22 |
| ✅ EXACT | `Action_SnapReceive` | QB | `25` | `24` | 27 | END | 18 | 27 |
| ✅ EXACT | `Action_Toss` | QB | `25` | `24` | 33 | START | 33 | 49 |
| ✅ EXACT | `Action_BallCarry` | RB | `20` | `19` | 50 | START | 50 | 140 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 3–85
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_None` | 28 | 32 | 5 | inferred_complete_timeline |
| `Action_Toss` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 85 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 3–140
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 49 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 140 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `28`</summary>

- **xml_track_id:** `27`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 3–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_CrackBlock` | 21 | 150 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `26`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 3–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–142
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 82 | 65 | inferred_complete_timeline |
| `Action_None` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 120 | 32 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 142 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_None` | 28 | 128 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 60 | 43 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 3–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_None` | 23 | 150 | 128 | inferred_complete_timeline |

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
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `27`</summary>

- **xml_track_id:** `26`
- **actor_track_id:** `27`
- **team_side:** `defense`
- **Visible Frames:** 3–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 58 | 41 | inferred_complete_timeline |
| `Action_None` | 61 | 150 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 73 | 56 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 150 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 3–150
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 134 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 111 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 3–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 79 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 96 | 79 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 150 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 3–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–40 | 41 | 2 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 51–59 | 9 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 54–94 | 33 | 3 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 67–150 | 84 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 75–150 | 71 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 95–150 | 56 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 100–150 | 44 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 132–138 | 4 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 77 targets track ID '105', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 55 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-111] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-128] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-60] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-142] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-58] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [21-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-59] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-61] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-94] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-84] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>