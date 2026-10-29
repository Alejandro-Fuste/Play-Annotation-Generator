# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_106`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 214: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '8' has invalid range: start=185, end=170. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '8' has invalid range: start=206, end=170. Clamping end to start.
> - Action 'Action_PreSnap' range [0-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-48] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [185-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-168] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [185-239] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-194] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-230] for track '27' has 2 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_None' has invalid start frame 246. Video range is [0, 239].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.