# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_79`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 160: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [208-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-180] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-239] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-201] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '28' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.