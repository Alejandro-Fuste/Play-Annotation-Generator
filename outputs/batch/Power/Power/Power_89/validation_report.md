# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_89`
- **Input XML**: `outputs/batch/Power/Power/Power_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 180: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 180: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [29-239] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-45] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-99] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-213] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-205] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-232] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [138-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-156] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-165] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-203] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-146] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-239] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [91-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-175] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-202] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-209] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-218] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '35' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.