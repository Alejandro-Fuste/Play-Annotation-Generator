# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_144`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_144/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '3' (RG) duration 97 frames exceeds threshold 90 frames [start=129, end=225].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 108 frames exceeds threshold 90 frames [start=118, end=225].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 108 frames exceeds threshold 90 frames [start=118, end=225].
> - Action 'Action_None' range [115-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-213] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [129-214] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [216-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [223-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [118-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [157-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-132] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-270] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-33] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-192] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-291] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-38] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-162] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-293] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-143] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-299] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-299] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-258] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-248] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '32' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.