# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_53`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [84–93], lower_priority='Action_ZoneBlock' annotated_start=87, effective_Action_ZoneBlock_start=94.
> - Action 'Action_None' range [84-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-229] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-276] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-255] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-273] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-247] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [249-255] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [257-282] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-240] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [243-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-284] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-148] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-230] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-245] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-288] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-251] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-265] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-167] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-182] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-268] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-276] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-291] for track '34' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.