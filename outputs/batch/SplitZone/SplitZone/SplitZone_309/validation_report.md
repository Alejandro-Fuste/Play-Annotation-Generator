# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_309`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_309/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '17' has invalid range: start=107, end=104. Clamping end to start.
> - Action 'Action_None' range [46-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-175] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-128] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-160] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-164] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-264] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [46-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [83-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-220] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-155] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-205] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [56-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [61-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [67-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-160] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-248] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-211] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '24' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.