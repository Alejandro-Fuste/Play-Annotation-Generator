# Play-Annotation-Generator Annotation Review — QuickScreens_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ScreenBlock` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_RunAfterCatch` | WR4 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 19 | START | 19 | 32 |
| ✅ EXACT | `Action_ScreenBlock` | WR3 | `0` | `0` | 32 | START | 32 | 133 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 32 | END | 19 | 32 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR4 | `2` | `2` | 34 | START | 34 | 69 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `18` | `18` | 50 | START | 50 | 58 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `2` | `2` | 72 | START | 72 | 82 |
| ✅ EXACT | `Action_RunAfterCatch` | WR4 | `2` | `2` | 91 | START | 91 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 150 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 74 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ScreenBlock` | 32 | 133 | 102 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 34 | 69 | 36 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_SecureCatch` | 72 | 82 | 11 | inferred_complete_timeline |
| `Action_None` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 91 | 103 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 150 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 60 | 42 | inferred_complete_timeline |
| `Action_None` | 72 | 150 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 54 | 36 | inferred_complete_timeline |
| `Action_None` | 56 | 74 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 33 | 41 | 9 | inferred_complete_timeline |
| `Action_None` | 43 | 150 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_None` | 53 | 64 | 12 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 139 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 43 | 25 | inferred_complete_timeline |
| `Action_None` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 62 | 150 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 131 | 113 | inferred_complete_timeline |
| `Action_None` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 66 | 48 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 98 | 10 | inferred_complete_timeline |
| `Action_None` | 103 | 150 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 53 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 95 | 77 | inferred_complete_timeline |
| `Action_None` | 103 | 110 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 113 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 69 | 51 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 99 | 81 | inferred_complete_timeline |
| `Action_None` | 101 | 134 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 134 | 116 | inferred_complete_timeline |
| `Action_None` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 42 | 24 | inferred_complete_timeline |
| `Action_None` | 44 | 100 | 57 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 138 | 15 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 118 | 100 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 6–150 | 61 | 9 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 38–85 | 47 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 44–62 | 16 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 48–49 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 51–150 | 100 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 55–89 | 10 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 78–150 | 73 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 84–150 | 67 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 88–150 | 46 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 113–139 | 24 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 118–150 | 33 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 135–150 | 16 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 138–150 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 78 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [134-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [91-103] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-131] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-33] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-150] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-43] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-64] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-74] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-38] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-64] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-139] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-62] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-96] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-120] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-134] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '34' has 1 frames without a visible bounding box.
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