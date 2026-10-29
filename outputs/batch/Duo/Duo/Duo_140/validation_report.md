# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_140`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [158-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [107-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-211] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-141] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-183] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-213] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-88] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-116] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-187] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-139] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-230] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-214] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.