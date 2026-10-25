# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_7`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 6, Column 'Run Block': Could not parse frame number from '-' in entry '-,OL'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [36-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-72] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-286] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-190] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-194] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-282] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-277] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-221] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-78] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-118] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-224] for track '29' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.