# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Duo_114`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_ComboBlock' at frame 464 targets track ID '28', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 230: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '20' has invalid range: start=464, end=118. Clamping end to start.
> - Action 'Action_PreSnap' range [0-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-46] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-213] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-44] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-61] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-15] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-163] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-208] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-222] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-233] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-239] for track '24' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_ComboBlock' has invalid start frame 464. Video range is [0, 239].
> - Action event 'Action_None' has invalid start frame 613. Video range is [0, 239].

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.