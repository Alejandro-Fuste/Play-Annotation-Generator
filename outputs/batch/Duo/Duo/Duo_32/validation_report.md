# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_32`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '3' has invalid range: start=520, end=239. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '7' has invalid range: start=520, end=132. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=520, end=239. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '15' has invalid range: start=547, end=239. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '20' has invalid range: start=520, end=239. Clamping end to start.
> - Action 'Action_PreSnap' range [0-208] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-204] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-192] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-157] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-239] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-13] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-196] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-239] for track '27' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_ComboBlock' has invalid start frame 520. Video range is [0, 239].
> - Action event 'Action_ComboBlock' has invalid start frame 520. Video range is [0, 239].
> - Action event 'Action_ComboBlock' has invalid start frame 520. Video range is [0, 239].
> - Action event 'Action_ComboBlock' has invalid start frame 520. Video range is [0, 239].
> - Action event 'Action_BlockSecondLevel' has invalid start frame 547. Video range is [0, 239].
> - Action event 'Action_None' has invalid start frame 566. Video range is [0, 239].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.