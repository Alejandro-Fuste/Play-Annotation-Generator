# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_203`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 168 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [129–142], lower_priority='Action_ZoneBlock' annotated_start=132, effective_Action_ZoneBlock_start=143.
> - Action 'Action_None' range [129-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-366] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [371-389] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-152] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-362] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-373] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-202] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '11' starts at frame 143, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [143-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-188] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [141-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-188] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-185] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-242] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-389] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-280] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-343] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [349-356] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-237] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-389] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-372] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-275] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-287] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-309] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-361] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-289] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-275] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-371] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-384] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-289] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [292-371] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-384] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-284] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-384] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [278-389] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-284] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-305] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-316] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-333] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-352] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-286] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-368] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-374] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-382] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [386-389] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-310] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-332] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-380] for track '47' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-341] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '50' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.