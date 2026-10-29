# Play-Annotation-Generator Annotation Review — Duo_219

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_219`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | QB | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ComboBlock` | WR2 | offense | `19` | `19` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 5 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 5 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 5 | START | 5 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 5 | START | 5 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 5 | START | 5 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 5 | START | 5 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 5 | START | 5 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `21` | `Group` | 5 | START | 5 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `23` | `Group` | 5 | START | 8 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 5 | START | 0 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | QB | `1` | `1` | 45 | START | 45 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `17` | `17` | 45 | START | 45 | 76 |
| ✅ EXACT | `Action_ComboBlock` | LT | `18` | `18` | 45 | START | 45 | 80 |
| ✅ EXACT | `Action_ComboBlock` | WR2 | `19` | `19` | 45 | START | 45 | 75 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `13` | `13` | 54 | START | 54 | 73 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 80 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ComboBlock` | 45 | 71 | 27 | inferred_complete_timeline |
| `Action_ComboBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 125 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 8–116
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 34 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 79 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 116 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–62
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 62 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–75
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_ComboBlock` | 45 | 75 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_ComboBlock` | 45 | 80 | 36 | inferred_complete_timeline |
| `Action_None` | 81 | 125 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–125
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_ComboBlock` | 45 | 76 | 32 | inferred_complete_timeline |
| `Action_ComboBlock` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 125 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 54 | 73 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `25`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 8–104
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 39 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 125 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 29 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 125 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–113
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 67 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 96 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 113 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–123
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 123 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–90 | 8 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–125 | 93 | 5 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 9–90 | 28 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 37–122 | 86 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 44–125 | 40 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 44–91 | 33 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 64–95 | 20 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 89–106 | 18 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 105–113 | 9 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 107–125 | 19 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 113–123 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [45-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [74-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-81] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-125] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-29] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [54-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [45-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [78-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-125] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [45-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [45-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-113] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-125] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-97] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-116] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-39] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-17] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-76] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-122] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-57] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-101] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-113] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-64] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-72] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-76] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-106] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-113] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-125] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-123] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>