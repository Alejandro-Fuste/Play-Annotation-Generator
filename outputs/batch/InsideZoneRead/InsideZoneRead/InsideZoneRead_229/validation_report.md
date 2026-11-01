# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_229`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_229/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [95–105], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=106.
> - Action 'Action_None' range [95-145] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-232] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [95-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-207] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [180-212] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-204] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-136] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-149] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-231] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [138-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [146-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-162] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [95-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-207] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-238] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-207] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '29' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.