# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_214`
- **Input XML**: `outputs/batch/Power/Power/Power_214/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 430: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [11-146] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-222] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-265] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-170] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-43] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-86] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '9' starts at frame 115, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [115-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-126] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-178] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-267] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-157] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-18] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-73] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-110] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-203] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-284] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-194] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-270] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-280] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.