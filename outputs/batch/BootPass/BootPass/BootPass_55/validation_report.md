# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_55`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [139–158], lower_priority='Action_RunBlock' annotated_start=148, effective_Action_RunBlock_start=159.
> - Segment 'Action_SecureCatch' for track '26' has invalid range: start=223, end=134. Clamping end to start.
> - Action 'Action_None' range [139-322] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-316] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-263] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [166-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [148-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [202-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [211-247] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-326] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [139-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [159-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [166-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [148-171] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-171] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-183] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-195] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [148-205] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [207-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' for track '21' starts at frame 148, but the player has no visible bounding box on this frame.
> - Action 'Action_RunBlock' range [148-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [156-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-266] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-291] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '31' has 1 frames without a visible bounding box.
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