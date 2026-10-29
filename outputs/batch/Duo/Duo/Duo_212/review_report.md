# Play-Annotation-Generator Annotation Review — Duo_212

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_212`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `31` | `22` |
| ✅ EXACT | `Action_ComboBlock` | TE2 | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 2 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | `15` | `15` | 89 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | `31` | `22` | 89 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | TE2 | `3` | `3` | 89 | START | 89 | 112 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | `8` | `8` | 89 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 112 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 150 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 150 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 94 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ComboBlock` | 89 | 112 | 24 | inferred_complete_timeline |
| `Action_None` | 113 | 150 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 13 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 150 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 10 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 79 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–5
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 13 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 52 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 72 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 116 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 74 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 113 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 150 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 91 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 150 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 131 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `25` | Position_Unknown | Team_Unknown | 26–44 | 11 | 3 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 48–86 | 39 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 62–66 | 5 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 64–150 | 84 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 67–150 | 83 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 69–89 | 14 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 73–150 | 62 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 74–150 | 40 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 90–132 | 43 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 91–150 | 60 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 92–150 | 48 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 124–150 | 27 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 137–150 | 9 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `15` (C)
- ❌ Missing segment for action `Action_ComboBlock` on target `22` (Position_Unknown)
- ❌ Missing segment for action `Action_ComboBlock` on target `8` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '8' has invalid range: start=89, end=52. Clamping end to start.
- ⚠️ Segment 'Action_ComboBlock' for track '15' has invalid range: start=89, end=79. Clamping end to start.
- ⚠️ Segment 'Action_ComboBlock' for track '22' has invalid range: start=89, end=66. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-91] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-150] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-13] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-13] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-150] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-72] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-116] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-10] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-79] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-74] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-94] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-86] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-66] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-91] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-79] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-82] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-107] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-150] for track '33' has 2 frames without a visible bounding box.
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