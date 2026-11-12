# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_241`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_241/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 484: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [98-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-208] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-257] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [105-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [168-171] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-217] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-244] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [98-109] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-261] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-159] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [165-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-254] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-230] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.